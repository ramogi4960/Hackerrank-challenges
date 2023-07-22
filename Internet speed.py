from speedtest import Speedtest

print(f"Download speed is: {Speedtest().download()/1000000}")
print(f"Upload speed is: {Speedtest().upload()/1000000}")