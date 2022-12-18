import speedtest


st = speedtest.Speedtest()

st.get_best_server()
print(f"Your ping is: {st.results.ping} ms")
print(f"Your download speed: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
print(f"Your upload speed: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")