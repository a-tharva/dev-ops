docker build -t python-ssh:entrypoint .

docker run --name python_test --rm -p 30001:22 -dit -e repo="https://github.com/binudhir/hello-world.git" python-ssh:entrypoint1