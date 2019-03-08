#include "rp_types.h"
#include "samples.h"
#include <gphoto2/gphoto2.h>

my_struct init_camera();
void capture_to_file(my_struct context, char *fn);
