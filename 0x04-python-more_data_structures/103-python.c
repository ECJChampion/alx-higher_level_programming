#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid Python List\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List: %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Python Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *bytes_data;

    printf("[.] bytes object info\n");
    printf("  Size: %ld\n", size);

    printf("  trying string: %s\n", PyUnicode_Check(p) ? "yes" : "no");

    if (size >= 10)
        size = 10;

    bytes_data = PyBytes_AsString(p);

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; ++i) {
        printf("%02hhx", bytes_data[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

