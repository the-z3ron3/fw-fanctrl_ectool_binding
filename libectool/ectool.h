#pragma once

// Type declarations
typedef struct BatteryInfo_t
{
    int capacity;
    float kilowatts;
} BatteryInfo_t;

// Function declarations
BatteryInfo_t get_battery_info(void);
int get_temperature(void);
void set_speed(int speed);
bool is_on_ac(void);
void pause(void);
