
# coding: utf-8

# ## Synchronous

# In[1]:


import distutils.dir_util
from distutils.dir_util import copy_tree
import glob
import time
x = glob.glob("/pythonSyncAsyncCopyDirectory/sync/*")

startTime = time.time()

def copy_sync(src, dst):
    print("From %s to %s." % (src, dst))
    distutils.dir_util._path_created = {}
    return copy_tree(src, dst)
  
def main():
    for i in range(len(x)):
        copy_sync(x[i],x[i]+"Copy")
    
main()
finishTime = time.time()
print("Total time:" + str(finishTime - startTime))


# ## Asynchronous

# In[2]:


import asyncio
import distutils.dir_util
from distutils.dir_util import copy_tree
import glob
import time
x = glob.glob("/pythonSyncAsyncCopyDirectory/async/*")
startTime = time.time()

async def copy_async(src, dst):
    print("From %s to %s." % (src, dst))
    distutils.dir_util._path_created = {}
    return copy_tree(src, dst)
  

async def main():
    for i in range(len(x)):
        await asyncio.wait([copy_async(x[i],x[i]+"Copy")])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
finishTime = time.time()
print("Total time:" + str(finishTime - startTime))

