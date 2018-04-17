import sys
from bitstring import BitArray

X1 = -12.0
X2 = 31.0
SUM = BitArray(length=32)

# if X1 < X2 - swap them
if (abs(X1) < abs(X2)):
    X1, X2 = X2, X1

X1_bits = BitArray(float=X1, length=32)
X2_bits = BitArray(float=X2, length=32)

E1 = X1_bits[1:9]
E2 = X2_bits[1:9]

M1 = BitArray(bin=('1'+X1_bits[9:].bin))
M2 = BitArray(bin=('1'+X2_bits[9:].bin))

print("X1 =", X1, "-->", X1_bits.bin, " ( sign: " + X1_bits.bin[0] + ", exponent: " + E1.bin + ", mantissa:", M1.bin + " )")
print("X2 =", X2, "-->", X2_bits.bin, " ( sign: " + X1_bits.bin[0] + ", exponent: " + E1.bin + ", mantissa:", M1.bin + " )")
print()

print("Sign of the result:", int(X1_bits[0] ^ X2_bits[0]))
print()

# initital exponent value of the reult
result_E = E1

# find exponent difference and shift M2 in order both numbers have similar exponent value
Exp_diff = E1.uint - E2.uint
print("Exponent difference: " + str(E1.uint) + " - " + str(E2.uint) + " = " + str(Exp_diff))
print("Left shift decimal point of M2 by the exponent difference:")
print("M2 before  -  " + M2.bin)
M2 >>= Exp_diff
print("M2 after   -  " + M2.bin)
print()

# finding mantissa of the result
Result_M = 0
diff = 0
if X1_bits[0] == X2_bits[0]:
    Result_M = BitArray(uint=(M1.uint + M2.uint), length=(M1.uint + M2.uint).bit_length())
    print("Adding M1 and M2, result mantissa:", Result_M.bin)
    # normalizing the resultant mantissa
    if Result_M.len > M1.len:
        diff = Result_M.len - M1.len
        del Result_M[Result_M.len - diff:]
        result_E[:] = result_E.int + diff
    print("Normalizing result matissa:", Result_M.bin)
    print("Correcting exponent value of the result:", E2.bin)
else:
    Result_M = BitArray(uint=(M1.uint - M2.uint), length=M1.len)
    print("Subtrsacting M2 from M1, result mantissa:", Result_M.bin)
    # normalizing the resultant mantissa
    if not Result_M.uint:
        result_E.uint = 0
    else:
        while Result_M.bin[0] == '0':
            Result_M <<= 1
            result_E[:] = result_E.uint - 1
    print("Normalizing result matissa:", Result_M.bin)
    print("Correcting exponent value of the result:", E2.bin)

if result_E.uint >= 255:
    print("Infinity")
    sys.exit()
elif result_E.uint == 0:
    print('0.0')
    sys.exit()
else:
    SUM = BitArray(bin=X1_bits.bin[0] + result_E.bin + Result_M[1:].bin)

print()
print("Result:", SUM.bin, "-->", str(SUM.float) + " ( sign: " + SUM.bin[0] + ", exponent: " + SUM.bin[1:9] + ", mantissa:", SUM.bin[9:] + " )")
