#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>

#define GPIO0_START_ADDR	0x44E07000
#define GPIO0_END_ADDR		0x44E09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

#define GPIO1_START_ADDR	0x4804C000
#define GPIO1_END_ADDR		0x4804E000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_DATAIN 0x138
#define USR2 (1<<23)
#define USR3 (1<<24)

int main() {
	volatile void *gpio0_addr;
	volatile unsigned int *gpio0_setdataout_addr;
	volatile unsigned int *gpio0_cleardataout_addr;

	volatile void *gpio1_addr;
	volatile unsigned int *gpio1_setdataout_addr;
	volatile unsigned int *gpio1_cleardataout_addr;

	volatile unsigned int *gpio0_datain_addr;
	volatile unsigned int *gpio1_datain_addr;

	int fd = open("/dev/mem", O_RDWR);
	gpio0_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
	gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

	if (gpio0_addr == MAP_FAILED)
		printf("map 0 failed\n");
	if (gpio1_addr == MAP_FAILED)
		printf("map 1 failed\n");

	gpio0_datain_addr = gpio0_addr + GPIO_DATAIN;
	gpio1_datain_addr = gpio1_addr + GPIO_DATAIN;

	gpio1_setdataout_addr = gpio1_addr + GPIO_SETDATAOUT;
	gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEARDATAOUT;

	//*gpio1_setdataout_addr = USR3;
	//*gpio1_setdataout_addr = USR2;
	//sleep(2);
	//*gpio1_cleardataout_addr = USR2;
	//*gpio1_cleardataout_addr = USR3;
	for (int i=0; i<20; i++) {
		printf("%d   %d\n", *gpio0_datain_addr, *gpio1_datain_addr);
		sleep(1);
	}

	munmap((void *)gpio0_addr, GPIO0_SIZE);
	munmap((void *)gpio1_addr, GPIO1_SIZE);
	close(fd);
}
