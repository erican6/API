headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjZjE1N2E1LTZmNDgtNGYwZC1hY2EwLTk1OGNjM2M1YmM0MSIsImlhdCI6MTU2ODgzNDkzMiwic3ViIjoiZGV2ZWxvcGVyLzViOGM3ZDI3LTQwOTAtZmQ1Zi01ZWEwLTgwMDExZmU0NWNmMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5Ljc3LjE2MC4yIl0sInR5cGUiOiJjbGllbnQifV19.ORxMfBIGfJEhgbSm0LGNFR7PwZMVR5qgSyuyil1HH4uVg_eREyg6vMAnm-5B-RwppBltFn-rLh9iAE_fB8jPUg'
}
import requests

testfile = open("TestFile_ExampleOutput.html","w")
response = requests.get("https://api.clashofclans.com/v1/players/%23YVOYV82J", headers=headers)
data=response.content
data_as_string=data.decode()
testfile.write(data_as_string)
testfile.close()
print("Complete")