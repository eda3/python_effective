
1. write_test_files(tmpdir)
2. reduce_map(tmp_dir) -> 
   1. generate_inputs(data_dir) -> inputs: PathInputData
   2. create_workers(inputs) -> List[LineCountWorkers]
   3. execute(workers) -> int
