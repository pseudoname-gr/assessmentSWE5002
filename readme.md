# Aircraft Simulation

This Python script simulates aircraft traffic control for an assessment. The simulation generates random aircraft requests and processes them according to certain rules, displaying sorting out the higher priority aircraft in run-time.

## Features

- Simulates aircraft landing and takeoff operations.
- Generates random aircraft requests including normal landings, takeoffs, and emergency landings.

## Conditions

A small airport, with low traffic, needs to maintain landings and takeoffs. To do so, it maintains two queues where planes requesting to land or to take off are added, respectively.
If a plane requesting landing has an urgent issue (malfunction, low fuel, etc.), it will be given the highest priority and allowed to land before any other landing request in the queue.
Takeoff will only be allowed if the landing queue is empty, to ensure that planes do not wait too long in the air before landing.