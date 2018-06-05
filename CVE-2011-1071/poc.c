#include <err.h>
#include <fnmatch.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char* argv[]) {
  size_t num_as;
  char* p;
  setlocale(LC_ALL, "en_US.UTF8");
  if (argc < 2) {
    errx(1, "Missing argument.");
  }
  num_as = atoi(argv[1]);
  if (num_as < 5) {
    errx(1, "Need 5.");
  }
  p = malloc(num_as);
  if (!p) {
    errx(1, "malloc() failed.");
  }
  memset(p, 'A', num_as);
  p[num_as - 1] = '\0';
  p[0] = 'f';
  p[1] = 'o';
  p[2] = 'o';
  p[3] = '.';
  fnmatch("*.anim[1-9j]", p, 0);
  return 0;
}