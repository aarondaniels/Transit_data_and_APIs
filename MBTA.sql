CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    route_number int default 1,
    id varchar(255) not null,
    bearing int not null,
    current_status varchar(20),
    current_stop_sequence INT null, 
    direction_id int not null,
    label varchar(255) default null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    occupancy_status varchar(255) default null,
    speed int default null,
    updated_at datetime null
);

