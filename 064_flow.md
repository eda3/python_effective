
1. write_test_files(tmpdir)
1. reduce_map(tmp_dir) -> result:int
   1. generate_inputs(data_dir) -> inputs: PathInputData
   1. create_workers(inputs) -> List[LineCountWorkers]
   1. execute(workers) -> int
1. print(result)
