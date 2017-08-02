## Build
<pre>
docker build -t examples .
</pre>

## Run
<pre>
docker run --name my_examples -p 8887:8888 -v `pwd`:/notebooks -it --rm examples
</pre>
