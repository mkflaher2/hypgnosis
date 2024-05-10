--json
local json = require('json')

--http variables

local http = require 'http'
local status = 200
local dataString = '{"direction":1,"speed":1.0,"color":{"r":1.0,"g":1.0,"b":1.0,"a":1.0}}'
local data = {}
local headers = {}

--goes from 1 to 10
local speed = 1

-- variable for rotating spiral
local theta = 0

local color = {}
color["r"] = 1
color["g"] = 1
color["b"] = 1
color["a"] = 1

-- text handling
local font = lovr.graphics.getDefaultFont()
font:setPixelDensity(1)

-- texture
local spiralTexture = lovr.graphics.newTexture('images/spiral.jpg')
local spiralShader = lovr.graphics.newShader('unlit', 'unlit')

-- managing both eye views
local currentView = 1

local function draw(pass)

    local position = vec3(lovr.headset.getPosition('head'))
    local direction = vec3(lovr.headset.getDirection('head'))
    local orientation = quat(lovr.headset.getOrientation('head'))

    local radius = 5
    local length = 10

    local basePos = position - direction * 5

    local x, y, z = basePos:unpack()

    local scale = vec3(1,1,1)

    local dx, dy, dz = direction:unpack()

    local rotationMatrix = lovr.math.newMat4(basePos, scale, orientation)
    local composedMatrix = rotationMatrix:rotate(theta, 0, 0, -1)
    local angle, ax, ay, az = composedMatrix:getOrientation()

    -- draw the cone
    pass:setColor(1,1,1)
    pass:setMaterial(spiralTexture)
    -- Pass:cone(position, scale, orientation, segments)
    --
    local r = color["r"]
    local g = color["g"]
    local b = color["b"]
    local a = color["a"]
   
    pass:setColor(r, g, b, a)
    pass:cone(x, y, z, radius, length, angle, ax, ay, az)
    pass:text(dataString, position + direction * 5 , 0.005, orientation)

end

local function checkForUpdates() -- a polling function, to be called in lovr.update

    local tempStatus

    tempStatus, dataString, headers = http.request('http://192.168.0.186:8081/state') --TODO: parametrize or expose URL
    if tempStatus then
        status = tempStatus

        if status == 200 then

            data = json.decode(dataString)
            speed = data['speed']
            color = data['color']
        end
    end
end

function lovr.update(dt)
    -- query the web API
    checkForUpdates()
    -- increment the spiral rotation angle
    theta = theta + speed * dt
end

function lovr.draw(pass)
    draw(pass)
end
