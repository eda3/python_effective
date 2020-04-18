### あまりよくない
1. write_test_files(tmpdir)
1. reduce_map(tmp_dir) -> result:int
   1. generate_inputs(data_dir) -> inputs: PathInputData
   1. create_workers(inputs) -> List[LineCountWorkers]
   1. execute(workers) -> int
1. print(result)

### ジェネリック
1. write_test_files(tmpdir)
1. config = {"data_dir": tmpdir}
1. reduce_map(LineCountWorker, PathInputData, config) -> result:int
   1. GenericWorker.create_workers(input_class, config) -> List["GenericWorker"]
       1. PathInputData.generate_inputs(config) -> str
   1. execute(workers:List[LineCountWorker]) -> int
1. print(result)
