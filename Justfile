# Run commands with: just <recipe>

DOCKER_CMD := "docker run -it -v.:/workspace:Z jsbimage"

# Default recipe
default:
  @just --list

docker:
  docker build -t jsbimage .

scenario1:
  {{DOCKER_CMD}} jsbsim --root=jsbsim --script=scripts/f16_runway_test.xml


