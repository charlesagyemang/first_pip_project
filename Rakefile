def read_file(file_name)
  f = File.open(file_name,"r")
  res = f.read().strip
  f.close()
  res
end

@app_name   = read_file("app_name.txt")
@version    = read_file("version.txt")
@executable = "dist/#{@app_name}-#{@version}-py3-none-any.whl"

task :cred do
  p  "APP NAME: #{@app_name}"
  p  "VERSION : #{@version}"
  p  "EXECUTABLE : #{@executable}"
end

task :run do
  `rm -rf build dist finneynie.egg-info`
  `python3 setup.py bdist_wheel`
end

task :clean do
  `rm -rf build dist finneynie.egg-info`
  puts `git add . && git commit -am "cleanup" && git push origin master`
end

task :install do
  puts `python3 -m pip install dist/#{@app_name}-#{@version}-py3-none-any.whl`
end


task :upload do
  puts `python3 -m twine upload dist/*`
end
