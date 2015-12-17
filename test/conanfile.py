from conans import ConanFile, CMake
import os

class HelloReuseConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "Hello/0.1@memsharded/testing"
   generators = "cmake"

   def build(self):
       cmake = CMake(self.settings)
       self.run('cmake . %s' % cmake.command_line)
       self.run("cmake --build . %s" % cmake.build_config)

   def test(self):
       # equal to ./bin/greet, but portable win: .\bin\greet
       self.run(os.sep.join([".","bin", "greet"]))