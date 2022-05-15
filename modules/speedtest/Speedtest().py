'Run in terminal the command "speedtest-cli" '

import speedtest
  
  
st = speedtest.Speedtest()

servers = st.get_servers()
print(servers)

print(st.download())
print(st.upload())

servernames =[]
st.get_servers(servernames)
print(st.results.ping)
