#include <stdio.h>
#include <stdlib.h>
#include "config.h"
#include "utils/math.h"
#include "utils/common.h"
#include "core/engine.h"

int main() {
    printf("App: %s\n", APP_NAME);
    int result = add(3, 4);
    init_engine();
    return 0;
}
