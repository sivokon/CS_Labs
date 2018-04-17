from bitstring import BitArray

multiplicand = 7
multiplier = 7

# bitlegth = number of bits in longer sequence + 1(bit for sign)
bitlength = (multiplicand.bit_length() + 1 if multiplicand.bit_length() > multiplier.bit_length() else multiplier.bit_length() + 1)

# even if one of numbers is negative, we will anyway multiply them as positive and add the sign in the end of the program
multiplicandBits = BitArray(int=(multiplicand if multiplicand > 0 else multiplicand*(-1)), length=bitlength)
multiplierBits = BitArray(int=(multiplier if multiplier > 0 else multiplier*(-1)), length=bitlength)

Register = BitArray(length=(bitlength)*2)

print("Start:   Register:", Register.bin, " Multiplier:", multiplierBits.bin, " Multiplicand:", multiplicandBits.bin)
print()

counter = 0
while counter < multiplierBits.len:
    print("Iteration", counter+1, ":")
    if multiplierBits[bitlength-1]:
        Register[:bitlength] = Register[:bitlength].int + multiplicandBits.int
        print("Least significant multiplier bit is '1': Register = Register + Multiplicand =", Register.bin)
    Register >>= 1
    print("Shift register right:", Register.bin)
    multiplierBits >>= 1
    print("Shift multiplier right:", multiplierBits.bin)
    counter += 1
    print("Register: ", Register.bin, " Multiplier: ", multiplierBits.bin, " Multiplicand: ", multiplicandBits.bin)
    print();

# checking sign of the result
if (multiplicand < 0 and multiplier > 0) or (multiplicand > 0 and multiplier < 0):
    Register = BitArray(int=Register.int*(-1), length=Register.length)
print("")
print("Result: ", Register.bin, "-->", Register.int)
