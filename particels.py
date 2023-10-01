import particlepy
import random

def draw_particels(particle_system, dt, x_pos):
        particle_system.update(delta_time=dt)
        for _ in range(5):
            particle_system.emit(
                particlepy.particle.Particle(
                                            shape=particlepy.shape.Circle(radius=5,angle=random.randint(0, 360),color=(240, 0, 0),alpha=255),
                                            position=(x_pos, 0),
                                            velocity=(random.uniform(-150, 150), random.uniform(-150, 150)),
                                            delta_radius=0.2
                                            )
                )