cmake_minimum_required(VERSION 3.10)
project(std_capabilities)
find_package(ament_cmake REQUIRED)

# install interface files
install(DIRECTORY interfaces
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
