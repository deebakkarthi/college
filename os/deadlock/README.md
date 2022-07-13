## Safety

		proc_n processes
		res_n resources

### Data structures

		avail[res_n]

Available number of instances of each resource

		max[proc_n][res_n]

Total number of instances needed by the process

This doesn't change

		alloc[proc_n][res_n]

Number of instances of a resources currently allocated to a process

		need[proc_n][res_n] = max[proc_n][res_n] - alloc[proc_n][res_n]

Number of instances of a resources further required to complete

		finish[proc_n]
	
Status of the processes

### Algorithm
	
	work = avail

	for i in processes:
		if need[i] <= work and finish[i] is False:
			finish[i] = True
			work = work + alloc
	
if no such i satisfies the condition then deadlock

if finish[] is True for all i's, then no deadlock

## Request
		proc_n processes
		res_n resources

### Data structures

		avail[res_n]

Available number of instances of each resource

		max[proc_n][res_n]

Total number of instances needed by the process

This doesn't change

		alloc[proc_n][res_n]

Number of instances of a resources currently allocated to a process

		need[proc_n][res_n] = max[proc_n][res_n] - alloc[proc_n][res_n]

Number of instances of a resources further required to complete

		finish[proc_n]
	
Status of the processes

		req[res_n]
	
Number of instances of each resources requested by some process P

### Algorithm

		if req <= need:
			if req <= avail:
				# Simulate giving P it's request
				avail = avail - req
				alloc = alloc + req
				need  = need - req

				# Check for safe sequence
				if not safety():

					# Reclaim if there is no safe sequence
					#after that
					avail = avail + req
					alloc = alloc - req
					need  = need + req
			else:
				Wait for resources
		else:
			Invalid request

## Running the programs
		
		make

Compiling safety alone

		make safety

Compiling request alone

		make request 

## Input format

### Safety
		proc_n res_n
		avail
		max[i]
		alloc[i]

### Safety
		proc_n res_n
		avail
		max[i]
		alloc[i]
		pid
		req
