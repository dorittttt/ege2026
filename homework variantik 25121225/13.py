ip = "241.184.128.0"
mask = "255.255.240.0"

bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
print(bin_ip)
print(bin_mask)
left = "11110001.10111000.1000"
k = 0
for i in range(2**12):
    right = bin(i)[2:].zfill(12)
    if right[-1] != right[-2]:
        k += 1
print(k)