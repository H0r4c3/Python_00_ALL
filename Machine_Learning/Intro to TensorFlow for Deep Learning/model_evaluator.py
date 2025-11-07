import tensorflow as tf
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

def load_model_with_metadata(model_path):
    """Load a saved model and its metadata if available"""
    try:
        # Load the model
        model = tf.keras.models.load_model(model_path)
        print(f"✅ Model loaded successfully from: {model_path}")
        
        # Try to load metadata
        metadata_path = model_path.replace('.keras', '_metadata.json')
        metadata = None
        
        if os.path.exists(metadata_path):
            try:
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                print(f"✅ Metadata loaded from: {metadata_path}")
            except Exception as e:
                print(f"⚠️ Could not load metadata: {e}")
        else:
            print(f"⚠️ No metadata file found at: {metadata_path}")
        
        return model, metadata
    
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None, None

def list_available_models(models_folder="models"):
    """List all available model files in the models folder"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_path = os.path.join(current_dir, models_folder)
    
    if not os.path.exists(models_path):
        print(f"❌ Models folder not found: {models_path}")
        return []
    
    model_files = []
    for file in os.listdir(models_path):
        if file.endswith('.keras') or file.endswith('.h5'):
            model_files.append(os.path.join(models_path, file))
    
    return model_files

def select_model_interactive():
    """Interactive model selection"""
    models = list_available_models()
    
    if not models:
        print("❌ No models found in the 'models' folder!")
        return None
    
    print("\n" + "="*60)
    print("AVAILABLE MODELS")
    print("="*60)
    
    for i, model_path in enumerate(models, 1):
        model_name = os.path.basename(model_path)
        model_size = os.path.getsize(model_path)
        model_date = datetime.fromtimestamp(os.path.getmtime(model_path))
        
        print(f"{i:2d}. {model_name}")
        print(f"    Size: {model_size:,} bytes")
        print(f"    Modified: {model_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
    
    while True:
        try:
            choice = input(f"Select a model (1-{len(models)}) or 'q' to quit: ").strip()
            
            if choice.lower() == 'q':
                return None
            
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(models):
                return models[choice_idx]
            else:
                print(f"❌ Please enter a number between 1 and {len(models)}")
        
        except ValueError:
            print("❌ Please enter a valid number or 'q' to quit")

def celsius_to_fahrenheit_formula(celsius_list):
    """Calculate correct Fahrenheit values using the formula: F = C * 1.8 + 32"""
    return [round(c * 1.8 + 32, 2) for c in celsius_list]

def evaluate_model_predictions(model, test_celsius_list):
    """Make predictions and compare with correct values"""
    print(f"\n" + "="*80)
    print("MODEL EVALUATION RESULTS")
    print("="*80)
    
    # Make predictions
    predictions = []
    for celsius in test_celsius_list:
        pred = model.predict(np.array([[celsius]]), verbose=0)
        predictions.append(round(pred[0][0], 2))
    
    # Calculate correct values
    correct_fahrenheit = celsius_to_fahrenheit_formula(test_celsius_list)
    
    # Calculate errors
    absolute_errors = [abs(pred - correct) for pred, correct in zip(predictions, correct_fahrenheit)]
    relative_errors = [(abs(pred - correct) / abs(correct)) * 100 if correct != 0 else 0 
                      for pred, correct in zip(predictions, correct_fahrenheit)]
    
    # Print results
    print(f"\nInput Celsius List:")
    print(f"celsius_list = {test_celsius_list}")
    
    print(f"\nModel Predictions List:")
    print(f"prediction_list = {predictions}")
    
    print(f"\nCorrect Fahrenheit List (Formula: F = C × 1.8 + 32):")
    print(f"correct_list = {correct_fahrenheit}")
    
    print(f"\nAbsolute Errors (|Prediction - Correct|):")
    print(f"error_list = {[round(err, 2) for err in absolute_errors]}")
    
    # Detailed comparison table
    print(f"\n" + "-"*80)
    print("DETAILED COMPARISON TABLE")
    print("-"*80)
    print(f"{'Input (°C)':>10} {'Predicted (°F)':>15} {'Correct (°F)':>13} {'Abs Error':>10} {'Rel Error (%)':>12}")
    print("-"*80)
    
    for i, celsius in enumerate(test_celsius_list):
        print(f"{celsius:>10.1f} {predictions[i]:>15.2f} {correct_fahrenheit[i]:>13.2f} "
              f"{absolute_errors[i]:>10.2f} {relative_errors[i]:>11.2f}%")
    
    # Summary statistics
    print("-"*80)
    print("SUMMARY STATISTICS")
    print("-"*80)
    mean_abs_error = np.mean(absolute_errors)
    max_abs_error = np.max(absolute_errors)
    mean_rel_error = np.mean(relative_errors)
    
    print(f"Mean Absolute Error: {mean_abs_error:.4f} °F")
    print(f"Maximum Absolute Error: {max_abs_error:.4f} °F")
    print(f"Mean Relative Error: {mean_rel_error:.4f} %")
    
    # Model performance assessment
    print(f"\nMODEL PERFORMANCE ASSESSMENT:")
    if mean_abs_error < 0.1:
        print("🟢 EXCELLENT: Very high accuracy")
    elif mean_abs_error < 0.5:
        print("🟡 GOOD: Good accuracy")
    elif mean_abs_error < 2.0:
        print("🟠 FAIR: Acceptable accuracy")
    else:
        print("🔴 POOR: Low accuracy, model may need retraining")
    
    return predictions, correct_fahrenheit, absolute_errors

def plot_comparison(celsius_list, predictions, correct_values):
    """Create visualizations comparing predictions vs correct values"""
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Predictions vs Correct Values
    plt.subplot(1, 3, 1)
    plt.plot(celsius_list, correct_values, 'b-o', label='Correct Formula', linewidth=2, markersize=6)
    plt.plot(celsius_list, predictions, 'r--s', label='Model Predictions', linewidth=2, markersize=6)
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Temperature (°F)')
    plt.title('Predictions vs Correct Values')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Prediction Errors
    plt.subplot(1, 3, 2)
    errors = [pred - correct for pred, correct in zip(predictions, correct_values)]
    plt.bar(range(len(errors)), errors, color=['red' if e > 0 else 'blue' for e in errors], alpha=0.7)
    plt.xlabel('Test Case Index')
    plt.ylabel('Prediction Error (°F)')
    plt.title('Prediction Errors by Test Case')
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    plt.grid(True, alpha=0.3)
    
    # Plot 3: Scatter plot
    plt.subplot(1, 3, 3)
    plt.scatter(correct_values, predictions, alpha=0.7, s=60)
    min_val = min(min(correct_values), min(predictions))
    max_val = max(max(correct_values), max(predictions))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Predictions')
    plt.xlabel('Correct Values (°F)')
    plt.ylabel('Model Predictions (°F)')
    plt.title('Predictions vs Correct (Scatter)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def get_test_data():
    """Get test data from user input or use default values"""
    print(f"\n" + "="*60)
    print("TEST DATA SELECTION")
    print("="*60)
    
    print("Choose an option for test data:")
    print("1. Use default test values")
    print("2. Enter custom Celsius values")
    print("3. Use extended range test")
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            # Default test values
            return [0, 10, 20, 30, 40, 50, 75, 100]
        
        elif choice == '2':
            # Custom values
            while True:
                try:
                    input_str = input("Enter Celsius values separated by commas (e.g., -10, 0, 25, 100): ")
                    celsius_values = [float(x.strip()) for x in input_str.split(',')]
                    return celsius_values
                except ValueError:
                    print("❌ Please enter valid numbers separated by commas")
        
        elif choice == '3':
            # Extended range test
            return [-50, -20, -10, 0, 10, 25, 37, 50, 75, 100, 150, 200]
        
        else:
            print("❌ Please enter 1, 2, or 3")

def display_model_info(metadata):
    """Display model information if metadata is available"""
    if not metadata:
        print("ℹ️ No model metadata available")
        return
    
    print(f"\n" + "="*60)
    print("MODEL INFORMATION")
    print("="*60)
    
    if 'version' in metadata:
        print(f"Model Version: {metadata['version']}")
    
    if 'timestamp' in metadata:
        print(f"Created: {metadata['timestamp']}")
    
    if 'training_epochs' in metadata:
        print(f"Training Epochs: {metadata['training_epochs']}")
    
    if 'best_learning_rate' in metadata:
        print(f"Learning Rate: {metadata['best_learning_rate']}")
    
    if 'dataset_size' in metadata:
        print(f"Training Dataset Size: {metadata['dataset_size']}")
    
    # Display validation metrics if available
    if 'validation' in metadata:
        val_metrics = metadata['validation']
        print(f"\nValidation Metrics:")
        if 'r2' in val_metrics:
            print(f"  R² Score: {val_metrics['r2']:.6f}")
        if 'mae' in val_metrics:
            print(f"  Mean Absolute Error: {val_metrics['mae']:.4f} °F")
        if 'rmse' in val_metrics:
            print(f"  Root Mean Squared Error: {val_metrics['rmse']:.4f} °F")

# =============================================================================
# MAIN SCRIPT EXECUTION
# =============================================================================

def main():
    """Main execution function"""
    print("🔍 TENSORFLOW MODEL EVALUATOR")
    print("=" * 60)
    print("This script evaluates saved TensorFlow models for Celsius to Fahrenheit conversion")
    
    # Step 1: Select model
    model_path = select_model_interactive()
    if model_path is None:
        print("👋 Goodbye!")
        return
    
    # Step 2: Load model and metadata
    model, metadata = load_model_with_metadata(model_path)
    if model is None:
        print("❌ Failed to load model. Exiting.")
        return
    
    # Step 3: Display model information
    display_model_info(metadata)
    
    # Step 4: Get test data
    test_celsius_list = get_test_data()
    
    # Step 5: Evaluate model
    predictions, correct_values, errors = evaluate_model_predictions(model, test_celsius_list)
    
    # Step 6: Ask for visualization
    show_plots = input(f"\nWould you like to see visualization plots? (y/n): ").strip().lower()
    if show_plots in ['y', 'yes']:
        plot_comparison(test_celsius_list, predictions, correct_values)
    
    # Step 7: Ask for another evaluation
    another = input(f"\nWould you like to evaluate with different test data? (y/n): ").strip().lower()
    if another in ['y', 'yes']:
        test_celsius_list = get_test_data()
        evaluate_model_predictions(model, test_celsius_list)
        
        show_plots = input(f"\nWould you like to see visualization plots? (y/n): ").strip().lower()
        if show_plots in ['y', 'yes']:
            plot_comparison(test_celsius_list, predictions, correct_values)
    
    print(f"\n✅ Evaluation completed!")
    print("📁 Model file:", os.path.basename(model_path))
    print("🎯 Use the printed lists in your code:")
    print("   - celsius_list: Input temperature values")
    print("   - prediction_list: Model predictions")
    print("   - correct_list: Formula-calculated correct values")

if __name__ == "__main__":
    main()