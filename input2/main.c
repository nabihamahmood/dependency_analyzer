#include <stdio.h>
#include "include/config.h"
#include "include/system.h"
#include "include/shared/macros.h"
#include "modules/utils/math.h"

int main() {
    print_app_info();
    int result = multiply(3, 4);
    printf("Result: %d\n", result);
    return 0;
}
