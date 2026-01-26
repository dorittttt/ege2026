ip = "143.168.72.213"
mask = "255.255.255.240"

bin_ip =[bin(int(i))[2:].zfill(8) for i in ip.split(".")]
bin_mask =[bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_ip)
print(bin_mask)
left = "10001111.10101000.01001000.11011110"
int_left = [int(i, 2) for i in left.split(".")]
print(*int_left, sep='')