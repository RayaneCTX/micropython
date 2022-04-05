/*
 * debug.c
 *
 * Author: Rayane G. Chatrieux
 * Date: Mar. 29, 2022
 */

#include "debug.h"


STATIC const char *const rule_name_table[] = {
#define DEF_RULE(rule, comp, kind, ...) #rule,
#define DEF_RULE_NC(rule, kind, ...)
#include "py/grammar.h"
#undef DEF_RULE
#undef DEF_RULE_NC
    "",
#define DEF_RULE(rule, comp, kind, ...)
#define DEF_RULE_NC(rule, kind, ...) #rule,
#include "py/grammar.h"
#undef DEF_RULE
#undef DEF_RULE_NC
};


void dbg_print_parse_node(mp_parse_node_t pn) {

    if(MP_PARSE_NODE_IS_NULL(pn)) {
        DPRINTF("pn = %p (null).\n", (void *) pn);
    }

    else if(MP_PARSE_NODE_IS_SMALL_INT(pn)) {
        int arg = (int) MP_PARSE_NODE_LEAF_SMALL_INT(pn);
        DPRINTF("pn = %p (small int %d).\n", (void *) pn, arg);
    }

    else if(MP_PARSE_NODE_IS_STRUCT(pn)) {
        mp_parse_node_struct_t *pns = (mp_parse_node_struct_t *) pn;
        int num_child = MP_PARSE_NODE_STRUCT_NUM_NODES(pns);
        int rule = (int) MP_PARSE_NODE_STRUCT_KIND(pns);
        char const *name = rule_name_table[rule];
        DPRINTF("pn = %p (rule '%s' with %d children).\n", (void *) pn, name, num_child);
    }

    else {
        uintptr_t arg = MP_PARSE_NODE_LEAF_ARG(pn);
        switch (MP_PARSE_NODE_LEAF_KIND(pn)) {
            case MP_PARSE_NODE_ID:
                DPRINTF("pn = %p (id '%s').\n", (void *) pn, qstr_str(arg));
                break;
            case MP_PARSE_NODE_STRING:
                DPRINTF("pn = %p (str '%s').\n", (void *) pn, qstr_str(arg));
                break;
            case MP_PARSE_NODE_BYTES:
                DPRINTF("pn = %p (bytes '%s').\n", (void *) pn, qstr_str(arg));
                break;
            default:
                assert(MP_PARSE_NODE_LEAF_KIND(pn) == MP_PARSE_NODE_TOKEN);
                DPRINTF("pn = %p (tok '%u').\n", (void *) pn, (uint) arg);
                break;
        }
    }

}
