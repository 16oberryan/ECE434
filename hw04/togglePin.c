#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>

#define GPIO1_START_ADDR	0x4804C000
#define GPIO1_END_ADDR		0x4804E000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define P8_16 (1<<14)

int main() {
	volatile void *gpio_addr;
	volatile unsigned int *gpio_setdataout_addr;
	volatile unsigned int *gpio_cleardataout_addr;

	int fd = open("/dev/mem", O_RDWR);
	gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

	if (gpio_addr == MAP_FAILED)
		printf("map failed\n");

	gpio_setdataout_addr = gpio_addr + GPIO_SETDATAOUT;
	gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

	for (int i=0; i<50000000; i++) {
		*gpio_setdataout_addr = P8_16;
		//usleep(1);
		*gpio_cleardataout_addr = P8_16;
		//usleep(1);
	}

	munmap((void *)gpio_addr, GPIO1_SIZE);
	close(fd);
}
