# casadi_codegeneration_example
Example of code generation from casadi and integration in simulink.

Run `example1.py` to generate C code from casadi. This will generate `test.c` and `test.h` files. 

Interface code has to be written manually. They are named `test_call.c` and `test_call.h`. Please refer to corresponding files for detail.

In simulink builder, Set `S-function name`. Then go to `Data Properties`. Add input ports `a` with 1 rows. Add output ports `x` and `y` with 1 rows each. Go to `Libraries` tab and add all the names of C files in `Library/Object/Source files`. Add `#include "HEADER.h"` in `Includes`. Go to `Outputs` tab and write code for function call. Click `build` button. The, simulink model can be run.