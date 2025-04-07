# Delete old library file
rm libectool.so

# Compile new library file
gcc -fPIC -c ectool.c -o ectool.o
gcc -shared -o libectool.so ectool.o

# Copy new library file into base fw-fanctrl folder
cp libectool.so ../libectool.so
