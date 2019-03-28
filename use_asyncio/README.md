### asyncio的功能
1. 包含各种特定系统实现的模块化事件循环
2. 传输和协议抽象
3. 对TCP，UDP，SSL，子进程，延时调用以及其他的具体支持
4. 模仿futures模块但适用于事件循环使用的future类
5. 基于yield from的协议和任务，可以让你用顺序的方式编写并发代码
6. 必须使用一个产生阻塞IO的调用时，有接口可以把这个事件转移到线程池
7. 模仿threading模块中的同步原语，可以用在单线程内的协程之间

### 扩展
python史上性能最高的web框架sanic，基于asyncio实现的