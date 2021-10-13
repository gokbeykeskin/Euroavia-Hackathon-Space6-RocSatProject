from vpython import *

def start_sattelite_sim(velocityV, velocityH, alt, sat_mass):
    G = 6.67e-11
    RE = 6.378e6
    ME = 5.972e24
    rate_val = 300

    earth = sphere(pos = vector(0, 0, 0), radius = RE, texture=textures.earth)
    earth.m = ME
    earth.p = earth.m * vector(0,0,0)

    sattelite = sphere(pos = (vector(RE + float(alt),0,0)), radius = .03*RE, make_trail = True)
    sattelite.m = float(sat_mass)
    sattelite.p = sattelite.m*vector(velocityV,velocityH,0)

    t = 0
    dt = 1

    gd1 = graph(
      title='<b>Time - Distance</b>',
      xtitle='<i>Time (s)</i>', ytitle='<i>Distance (m)</i>',
        background=color.black, align = 'right')
    length_graph = gcurve(graph = gd1, color = color.purple)

    gd2 = graph(
      title='<b>Time - Velocity</b>',
      xtitle='<i>Time (s)</i>', ytitle='<i>Velocity (m/s)</i>',
        background=color.black)
    velocity_graph = gcurve(graph = gd2, color = color.purple)
    
    while True:    
        rate(rate_val)
        r = sattelite.pos - earth.pos
        F=-G*earth.m * sattelite.m * norm(r) / mag(r)**2
        sattelite.p = sattelite.p + F*dt
        sattelite.pos = sattelite.pos + sattelite.p*dt / sattelite.m
        t=t+dt
        length_graph.plot(t, mag(sattelite.pos))
        velocity_graph.plot(t, mag(sattelite.p / sattelite.m))
        if mag(r) <= RE:
            L = label()
            L.text = """Sattelite crash!"""
            break
