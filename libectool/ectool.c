#include <stdlib.h>         // for rand(), srand()
#include <stdbool.h>        // for bool
#include <time.h>           // for time()
#include "ectool.h"         // structure and function declarations

BatteryInfo_t get_battery_info(void)
{
    BatteryInfo_t battery_info = {0};

    // Fill BatteryInfo_t struct members
    battery_info.capacity = rand() % 101;
    battery_info.kilowatts = rand() % 5001;

    return (battery_info);
}

int get_temperature(void)
{
    // Seed the random number generator with current time
    srand(time(NULL));

    // Generate a random number between 15 and 70
    int temperature = rand() % (15 - 70 + 1) + 15;

    return (temperature);
}

void set_speed(int speed)
{
    // Logic to change fan speed to passed `speed` parameter
    int speed_set = speed;
}

bool is_on_ac(void)
{
    // Seed the random number generator with current time
    srand(time(NULL));

    // Generate a random number between 0 and 2
    int rand_bool = rand() % 2;

    bool ac_value = false;
    
    // Flipping boolean value
    if (rand_bool == true)
    {
        ac_value = true;
    }

    return (ac_value);
}

void pause(void)
{
    bool fan_paused = true;
}
