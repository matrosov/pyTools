import sys
import array

def plug_check(bytearr):
    id = bytearr[0:3]
    key = bytearr[7:14]
    id_hex= ""
    key_hex = ""
    
    for i in id:
        id_hex += "%02x " %i
    for i in key:
        key_hex += "%02x " %i
        
    print "Signature: " + id_hex
    print "Key: " + key_hex
    return key

def decrypt(bytearr, key):
    b = []
    for i in range(len(bytearr) - 14):
        for k in range(len(key)):
            key_byte = int(key[k])
            
            byte = (i * k) & 0xFFFFFFFF
            key_byte = (key_byte + byte) & 0xFF
            
            byte = bytearr[i + 14]
            z = byte ^ key_byte
            bytearr[i + 14] = z
        b.append(bytearr[i + 14])
    return b
        
    
def main(file, out):
    f = open(file, "rb")
    bytearr = map(ord, f.read())
    f.close()
    
    o = open(out, "wb").write(array.array("B",(decrypt(bytearr, plug_check(bytearr)))))
    
if (len(sys.argv) == 3):
    main(sys.argv[1], sys.argv[2])
else:
    print "Usage: %s <carberp_plugin> <output_file>" % (sys.argv[0])