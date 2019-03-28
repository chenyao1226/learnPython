import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED, ALL_COMPLETED

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers = 2)  # 定义一个线程池
'''
通过submit提交的任务会立即返回，不会阻塞程序
'''
task1 = executor.submit(get_html, (1))
task2 = executor.submit(get_html, (2))

print(task1.done())  # done查看任务的是否已经执行完成
print(task2.cancel()) # cancel可以取消任务
print(task1.result())  # 可以拿到任务的执行结果


print("+++++++++++++++++++++++++++++++")

urls = [3,2,4]
all_task = [executor.submit(get_html, (url)) for url in urls]
'''
wait方法会阻塞程序，知道接收到返回值return_when, renturn_when支持三种模式
    FIRST_COMPLETED
    FIRST_EXCEPTION
    ALL_COMPLETED
'''
wait(all_task, return_when=ALL_COMPLETED)

'''
as_completed 方法会阻塞程序，直到所有的线程都完成
'''
# for future in as_completed(all_task):
#     data = future.result()
#     print("{} get page".format(data))
#
'''
通过executor的map获取已经完成的task的值(线程的返回值)
'''
for data in executor.map(get_html, urls):
    print("{} get page".format(data))

''' concurrent.futures中有一个很重要的类Future，通过ThreadPoolExecutor提交一个任务之后会返回这个类，正式通过这个类
我们才可以控制任务的执行过程，需要仔细研究一下这个类的源码
'''
from concurrent.futures import Future