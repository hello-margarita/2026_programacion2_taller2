# Dental Clinic Appointments - Queues

Console-based clinic appointment management system built with Python (queues, OOP, and input validation) for a Programming II course at Universidad de Manizales (2026).

This is Workshop 2. It reuses the client registration and validation code from Workshop 1 and adds queues to manage the appointments.

## What the program does

- Registers clients one by one, validating every field: ID number, name, phone, client type, treatment, quantity, priority, and appointment date.
- Calculates the total price of each appointment based on the client type (private, EPS, or prepaid) and the treatment (cleaning, fillings, extraction, or diagnosis).
- Keeps two queues, both sorted by appointment date (the closest date goes first):
  - **Urgent extractions:** clients who come for an extraction and are marked as urgent.
  - **Daily agenda:** all the other clients.
- Each client is in only one queue at a time.

## Menu options

1. Register client
2. List all waiting clients (urgent and daily agenda), with the total to collect
3. Urgent extractions report, with the total to collect
4. Check the next urgent client
5. Attend the next urgent client
6. List the daily agenda, with the total to collect
7. Check the next client in the daily agenda
8. Attend the next client in the daily agenda
9. Exit

When a client is attended, they leave the queue.

## How the queues work

- The queues are made with `deque` from the `collections` module. Only `append`, `popleft`, `[0]` (to see the first one) and `for` are used. No stacks are used.
- To keep a queue sorted by date, the program takes everyone out of the queue into an auxiliary list and puts them back in order, placing the new client in the right spot. If two clients have the same date, the one who arrived first stays first.
- The text date (DD/MM/YYYY) is converted to a number (YYYYMMDD) so dates can be compared correctly.

## Things to know

- A client can book more than one appointment with the same ID number. Each appointment is registered separately, and the program does not check for repeated ID numbers.
- The appointment date must be today or later. There is no upper limit.
- The data is only kept while the program is running (nothing is saved to a file).

## How to run it

You need Python 3. From the project folder, run:

```
python consultorio_odontologico_colas.py
```

## Author

Margarita María Arango Vélez - 2026