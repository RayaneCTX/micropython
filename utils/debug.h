/*
 * debug.h
 *
 * Author: Rayane G. Chatrieux
 * Date: Feb. 21, 2022
 */
#ifndef MICROPY_INCLUDED_PY_DEBUG_H
#define MICROPY_INCLUDED_PY_DEBUG_H

#include <stdio.h>

#define DPRINTF(...) do { \
        fprintf(stderr, "[%s: %d] %s(): ", __FILE__, __LINE__, __func__); \
        fprintf(stderr, __VA_ARGS__); \
    } while(0)

#endif
