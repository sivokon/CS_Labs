from bitstring import BitArray

inputDividend = 7
inputDivisor = 2

dividend = inputDividend if inputDividend > 0 else inputDividend*(-1)
divisor = inputDivisor if inputDivisor > 0 else inputDivisor*(-1)

# bitlegth = number of bits in longer sequence + 1(bit for sign)
bitlength = (dividend.bit_length() + 1 if dividend.bit_length() > divisor.bit_length() else divisor.bit_length() + 1)

dividendBits = BitArray(int=dividend, length=bitlength)
divisorBits = BitArray(int=divisor, length=bitlength)
QuotientBits = BitArray(length=bitlength)
RemainderBits = BitArray(int=dividend, length=bitlength*2)

print("Start:   Remainder:", RemainderBits.bin, " Quotient:", QuotientBits.bin, " Divisor:", divisorBits.bin, " Dividend:", dividendBits.bin)
print("")

counter = 0
arr = BitArray(length=bitlength+1)

while counter < bitlength:
    print("Iteration", counter+1, ":")
    RemainderBits <<= 1
    print("Shift remainder register to the left:", RemainderBits.bin)
    arr[:] = RemainderBits[:bitlength].int + divisor*(-1)
    RemainderBits[:bitlength] = arr[arr.len-bitlength:]
    print("Remainder = Remainder (left half) - divisor =", RemainderBits.bin)

    QuotientBits <<= 1
    if RemainderBits.int < 0:
        arr[:] = RemainderBits[:bitlength].int + divisor
        RemainderBits[:bitlength] = arr[arr.len-bitlength:]
        print("Remainder < 0:")
        print("  1) restor reminder value: Remainder = Remainder (left half) + divisor =", RemainderBits.bin)
        print("  2) shift quotient to the left and set the new least significant bit to 0:", QuotientBits.bin)
    else:
        QuotientBits.int += 1
        print("Remainder > 0:")
        print("  Shift quotient register to the left and set the new least significant bit to 1:", QuotientBits.bin)

    counter += 1
    print("Remainder:", RemainderBits.bin, " Quotient:", QuotientBits.bin, " Divisor:", divisorBits.bin)
    print()

# checking sign of the result
if (inputDividend < 0 and inputDivisor > 0) or (inputDividend > 0 and inputDivisor < 0):
    QuotientBits = BitArray(int=QuotientBits.int*(-1), length=QuotientBits.length)
print("")
print("Quotient:", QuotientBits.bin, "-->", QuotientBits.int, "   Remainder:", RemainderBits[:bitlength].bin, "-->", RemainderBits[:bitlength].int)



