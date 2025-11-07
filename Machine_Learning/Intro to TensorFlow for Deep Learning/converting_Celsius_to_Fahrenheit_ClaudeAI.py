import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import logging
import os
import json
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Try different import paths for callbacks (compatibility with different TF versions)
try:
    from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
except ImportError:
    try:
        from keras.callbacks import EarlyStopping, ReduceLROnPlateau
    except ImportError:
        from tensorflow.python.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Set up logging
logging.basicConfig(level=logging.ERROR)

def save_model_with_metadata(model, version, metrics, history=None):
    """Save model with metadata and training history"""
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_folder = os.path.join(current_dir, 'models')
    os.makedirs(models_folder, exist_ok=True)
    
    # Create versioned filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_name = f"celsius_fahrenheit_v{version}_{timestamp}.keras"
    model_path = os.path.join(models_folder, model_name)
    
    # Save the model
    model.save(model_path)
    print(f"Model saved at {model_path}")
    
    # Save metadata
    metadata = {
        'version': version,
        'timestamp': timestamp,
        'metrics': metrics,
        'model_path': model_path,
        'training_history': history.history if history else None
    }
    
    metadata_path = model_path.replace('.keras', '_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2, default=str)
    
    print(f"Metadata saved at {metadata_path}")
    return model_path

def evaluate_model(model, test_celsius, test_fahrenheit, model_name="Model"):
    """Comprehensive model evaluation"""
    predictions = model.predict(test_celsius, verbose=0).flatten()
    test_fahrenheit = np.array(test_fahrenheit).flatten()
    
    # Calculate metrics using NumPy (more reliable)
    mae = np.mean(np.abs(test_fahrenheit - predictions))
    mse = np.mean(np.square(test_fahrenheit - predictions))
    rmse = np.sqrt(mse)
    
    # R² score
    ss_res = np.sum(np.square(test_fahrenheit - predictions))
    ss_tot = np.sum(np.square(test_fahrenheit - np.mean(test_fahrenheit)))
    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    metrics = {
        'mae': float(mae),
        'mse': float(mse),
        'rmse': float(rmse),
        'r2': float(r2)
    }
    
    print(f"\n{model_name} Evaluation Metrics:")
    print(f"Mean Absolute Error: {mae:.4f}°F")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}°F")
    print(f"R² Score: {r2:.6f}")
    
    return metrics

def compare_results(model, input_celsius_list):
    """Compare model predictions with correct values"""
    correct_fahrenheit_list = [(c * 1.8 + 32) for c in input_celsius_list]
    predictions = model.predict(np.array(input_celsius_list), verbose=0)
    prediction_list_float = [round(pred[0], 2) for pred in predictions]
    
    print(f'\nComparison Results:')
    print(f'Input Celsius: {input_celsius_list}')
    print(f'Model Predictions (°F): {prediction_list_float}')
    print(f'Correct Values (°F): {correct_fahrenheit_list}')
    print(f'Absolute Errors: {[abs(pred - actual) for pred, actual in zip(prediction_list_float, correct_fahrenheit_list)]}')

def plot_comprehensive_results(history, model, celsius_range=(-50, 150)):
    """Create comprehensive visualization of training and predictions"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Training Loss
    axes[0, 0].plot(history.history['loss'], label='Training Loss', linewidth=2)
    if 'val_loss' in history.history:
        axes[0, 0].plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
    axes[0, 0].set_xlabel('Epoch')
    axes[0, 0].set_ylabel('Loss (MSE)')
    axes[0, 0].set_title('Training History')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Predictions vs Actual
    test_celsius = np.linspace(celsius_range[0], celsius_range[1], 200)
    predictions = model.predict(test_celsius, verbose=0).flatten()
    actual = test_celsius * 1.8 + 32
    
    axes[0, 1].plot(test_celsius, actual, 'b-', label='Actual Formula', linewidth=2)
    axes[0, 1].plot(test_celsius, predictions, 'r--', label='ML Predictions', linewidth=2)
    axes[0, 1].set_xlabel('Celsius (°C)')
    axes[0, 1].set_ylabel('Fahrenheit (°F)')
    axes[0, 1].set_title('Model Predictions vs Actual')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Prediction Error
    error = predictions - actual
    axes[1, 0].plot(test_celsius, error, 'g-', linewidth=2)
    axes[1, 0].axhline(y=0, color='k', linestyle='--', alpha=0.5)
    axes[1, 0].set_xlabel('Celsius (°C)')
    axes[1, 0].set_ylabel('Prediction Error (°F)')
    axes[1, 0].set_title('Prediction Error Distribution')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Error Histogram
    axes[1, 1].hist(error, bins=30, alpha=0.7, color='orange', edgecolor='black')
    axes[1, 1].axvline(x=0, color='r', linestyle='--', linewidth=2)
    axes[1, 1].set_xlabel('Prediction Error (°F)')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Error Distribution Histogram')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def create_model(learning_rate=0.1, units=1, use_regularization=False):
    """Create and compile model with optional regularization"""
    if use_regularization:
        model = tf.keras.Sequential([
            tf.keras.Input(shape=(1,)),
            tf.keras.layers.Dense(
                units=units, 
                kernel_regularizer=tf.keras.regularizers.l2(0.01)
            )
        ])
    else:
        model = tf.keras.Sequential([
            tf.keras.Input(shape=(1,)),
            tf.keras.layers.Dense(units=units)
        ])
    
    model.compile(
        loss='mean_squared_error',
        optimizer=tf.keras.optimizers.Adam(learning_rate),
        metrics=['mae']
    )
    
    return model

def hyperparameter_tuning(X_train, y_train, X_val, y_val):
    """Perform basic hyperparameter tuning"""
    print("\nPerforming hyperparameter tuning...")
    
    learning_rates = [0.01, 0.05, 0.1, 0.2]
    best_loss = float('inf')
    best_lr = None
    best_model = None
    
    results = []
    
    for lr in learning_rates:
        print(f"Testing learning rate: {lr}")
        model = create_model(learning_rate=lr)
        
        # Use early stopping for tuning
        early_stopping = EarlyStopping(patience=50, restore_best_weights=True, verbose=0)
        
        history = model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=500,
            callbacks=[early_stopping],
            verbose=0
        )
        
        final_val_loss = min(history.history['val_loss'])
        results.append((lr, final_val_loss))
        
        if final_val_loss < best_loss:
            best_loss = final_val_loss
            best_lr = lr
            best_model = model
    
    print(f"\nHyperparameter Tuning Results:")
    for lr, loss in results:
        print(f"Learning Rate: {lr:>6.3f} -> Validation Loss: {loss:.6f}")
    
    print(f"\nBest learning rate: {best_lr} with validation loss: {best_loss:.6f}")
    return best_model, best_lr

# =============================================================================
# MAIN SCRIPT
# =============================================================================

print("=== Enhanced Celsius to Fahrenheit ML Model ===\n")

# 1. CREATE ENHANCED DATASET
print("1. Creating enhanced dataset...")
celsius_q = np.array([
    -50, -40, -30, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 
    45, 50, 60, 70, 80, 90, 100, 110, 120, 150
], dtype=float)

fahrenheit_a = np.array([c * 1.8 + 32 for c in celsius_q], dtype=float)

print(f"Dataset size: {len(celsius_q)} data points")
print("Sample conversions:")
for i in range(0, len(celsius_q), 5):
    print(f'{celsius_q[i]:>6.1f}°C = {fahrenheit_a[i]:>6.1f}°F')

# 2. SPLIT DATA
print(f"\n2. Splitting data for training and validation...")
X_train, X_val, y_train, y_val = train_test_split(
    celsius_q, fahrenheit_a, test_size=0.2, random_state=42
)

print(f"Training set size: {len(X_train)}")
print(f"Validation set size: {len(X_val)}")

# 3. HYPERPARAMETER TUNING
best_model, best_lr = hyperparameter_tuning(X_train, y_train, X_val, y_val)

# 4. TRAIN FINAL MODEL WITH BEST PARAMETERS
print(f"\n3. Training final model with learning rate: {best_lr}")

# Create final model with best hyperparameters
final_model = create_model(learning_rate=best_lr, units=1)

# Set up callbacks
callbacks = [
    EarlyStopping(patience=100, restore_best_weights=True, verbose=1),
    ReduceLROnPlateau(patience=50, factor=0.5, min_lr=0.001, verbose=1)
]

# Train the final model
print("Training the final model...")
history = final_model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=1000,
    callbacks=callbacks,
    verbose=0
)

print('Finished training the final model')

# 5. EVALUATE MODEL
print(f"\n4. Evaluating model performance...")

# Evaluate on training set
train_metrics = evaluate_model(final_model, X_train, y_train, "Training Set")

# Evaluate on validation set
val_metrics = evaluate_model(final_model, X_val, y_val, "Validation Set")

# Test on extended range
test_celsius_extended = np.array([-100, -50, 0, 25, 50, 100, 200, 300, 500])
test_fahrenheit_extended = test_celsius_extended * 1.8 + 32
extended_metrics = evaluate_model(final_model, test_celsius_extended, test_fahrenheit_extended, "Extended Range Test")

# 6. SAVE MODEL WITH METADATA
print(f"\n5. Saving model and metadata...")
all_metrics = {
    'training': train_metrics,
    'validation': val_metrics,
    'extended_test': extended_metrics,
    'best_learning_rate': best_lr,
    'training_epochs': len(history.history['loss']),
    'dataset_size': len(celsius_q)
}

model_path = save_model_with_metadata(final_model, "2.0", all_metrics, history)

# 7. DETAILED PREDICTIONS COMPARISON
print(f"\n6. Detailed predictions comparison...")
test_values = [30, 50, 70, 80, 90, 120, 200, 400, 750, 1000]
compare_results(final_model, test_values)

# 8. DISPLAY MODEL ARCHITECTURE AND WEIGHTS
print(f"\n7. Model architecture and learned parameters...")
print("Model Summary:")
final_model.summary()

# Get the learned weights
layer_weights = final_model.layers[0].get_weights()
weight = layer_weights[0][0][0]  # The slope
bias = layer_weights[1][0]       # The intercept

print(f"\nLearned Parameters:")
print(f"Weight (slope): {weight:.6f} (Expected: ~1.8)")
print(f"Bias (intercept): {bias:.6f} (Expected: ~32.0)")
print(f"Learned formula: F = {weight:.6f} * C + {bias:.6f}")
print(f"Actual formula:  F = 1.800000 * C + 32.000000")

# 9. VISUALIZATIONS
print(f"\n8. Creating comprehensive visualizations...")
plot_comprehensive_results(history, final_model)

# 10. FINAL SUMMARY
print(f"\n" + "="*60)
print("FINAL MODEL SUMMARY")
print("="*60)
print(f"Model Version: 2.0")
print(f"Dataset Size: {len(celsius_q)} points")
print(f"Training Points: {len(X_train)}")
print(f"Validation Points: {len(X_val)}")
print(f"Best Learning Rate: {best_lr}")
print(f"Training Epochs: {len(history.history['loss'])}")
print(f"Final Training Loss: {history.history['loss'][-1]:.6f}")
print(f"Final Validation Loss: {history.history['val_loss'][-1]:.6f}")
print(f"Validation R² Score: {val_metrics['r2']:.6f}")
print(f"Model saved at: {model_path}")
print("="*60)

print("\nModel training and evaluation completed successfully!")