ip = "172.16.160.0"
mask = "255.255.240.0"
k = 0
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
print(bin_ip)
print(bin_mask)
left = "10101100000100001010"
for i in range(2**12):
    right  = bin(i)[2:].zfill(12)
    if (left + right).count("1") % 2 == 0:
        k += 1
print(k)