import cubes
import cProfile


if __name__ == "__main__":
    cProfile.run("cubes.generate_polycubes(8, use_cache=False)")