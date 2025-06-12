#ifndef LOGGER_H
#define LOGGER_H

#include <stdio.h>

static void log_info(const char *msg) {
    printf("[INFO] %s\n", msg);
}

#endif
