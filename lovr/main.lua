-- json
local json = require('json')

-- http variables

local http = require 'http'
local status = 200
local dataString = '{"direction":1,"speed":1.0,"color":{"r":1.0,"g":1.0,"b":1.0,"a":1.0}}'
local headers = {}

local pollTime = 0

-- debug variable
local pollCount = 0

--goes from 1 to 10
local speed = 1
local nextSpeed = 1

-- variables for rotating spiral
local frameTime = 0
local theta = 0

-- color vars

local r = 1
local g = 1
local b = 1
local a = 1

local nextR = 1
local nextG = 1
local nextB = 1
local nextA = 1

-- text handling
local font = lovr.graphics.newFont('fonts/DejaVuSansMono.ttf')
font:setPixelDensity(1)

-- texture
local spiralTexture = lovr.graphics.newTexture('images/spiral.jpg')
local spiralShader = lovr.graphics.newShader('unlit', 'unlit')

-- managing both eye views
local currentView = 1

-- state machine
local state = "waiting_room"

-- user ID for communicating with API
local userId = ""

function waiting_room(pass)
    -- head position, direction, and orientation
    local position = vec3(lovr.headset.getPosition('head'))
    local direction = vec3(lovr.headset.getDirection('head'))
    local orientation = quat(lovr.headset.getOrientation('head'))

    pass:setColor(1, 1, 1, 1)

    local message = "Please navigate to \n hypgnosis.solarized-dark.net \n and enter the collowing code: \n "
    local message = message .. userId

    pass:setFont(font)
    pass:text(message, position + direction * 1, 0.002, orientation)

end

function hypno_room(pass)

    -- head position, direction, and orientation
    local position = vec3(lovr.headset.getPosition('head'))
    local direction = vec3(lovr.headset.getDirection('head'))
    local orientation = quat(lovr.headset.getOrientation('head'))

    -- cone dimensions (the hypno spiral is textured on a cone that the viewer sees the inside of)
    local radius = 5
    local length = 10

    -- base position of the cone
    local basePos = position - direction * 5
    local x, y, z = basePos:unpack()

    local scale = vec3(1,1,1)

    -- update colors over 30 frames
    if r ~= nextR then
        r = r + (nextR - r) / 30
    end
    if g ~= nextG then
        g = g + (nextG - g) / 30
    end
    if b ~= nextB then
        b = b + (nextB - b) / 30
    end
    if a ~= nextA then
        a = a + (nextA - a) / 30
    end

    -- transition speed over 30 frames
    if speed ~= nextSpeed then
        speed = speed + (nextSpeed - speed) / 30
    end

    local timeDiff = lovr.headset.getTime() - frameTime
    frameTime = lovr.headset.getTime()
    theta = theta + speed * timeDiff

    -- rotation math
    local rotationMatrix = lovr.math.newMat4(basePos, scale, orientation)
    local composedMatrix = rotationMatrix:rotate(theta, 0, 0, -1)
    local angle, ax, ay, az = composedMatrix:getOrientation()


    -- draw the cone
    pass:setMaterial(spiralTexture)
    pass:setColor(r, g, b, a)
    pass:cone(x, y, z, radius, length, angle, ax, ay, az)

    --debug
    --pass:setColor(1,0,0)
    --pass:text(
    --    'speed ' .. speed .. ' theta ' .. theta .. ' r ' .. r .. ' g ' .. g .. ' b ' .. b .. ' a ' .. a .. '\n' ..
    --    'nextSpeed ' .. nextSpeed .. ' nextR ' .. nextR .. ' nextG ' .. nextG .. ' nextB ' .. nextB .. ' nextA ' .. nextA .. '\n' ..
    --    'pollCount ' .. pollCount .. '\n' .. 
    --    'timeDiff ' .. timeDiff .. '\n' ..
    --    'frameTime ' .. frameTime,
    --    position + direction * 1,
    --    0.001,
    --    orientation
    --)

end

function checkForUpdates() -- a polling function, to be called in lovr.update

    --prod
    --local tempStatus, dataString, headers = http.request(string.format('http://35.245.74.110:8081/users/%s', userId))
    --dev
    local tempStatus, dataString, headers = http.request(string.format('http://192.168.0.186:8081/users/%s', userId))

    local colorData = {}
    if tempStatus then
        status = tempStatus

        if status == 200 then

            data = json.decode(dataString)

            if data["user_id"] == userId then
                state = "hypno_room"
            else
                state = "waiting_room"
            end

            nextSpeed = data['speed']
            colorData = data['color']
        end

        nextR = colorData['r']
        nextG = colorData['g']
        nextB = colorData['b']
        nextA = colorData['a']
    end
end

function getUserId()
    local chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    userId = ""

    for i=1,6 do
        local rint = math.random(1, #chars)
        local rchar = chars:sub(rint, rint)
        userId = userId .. rchar
    end
end

function lovr.load(pass)
    getUserId()
end

function lovr.update(dt)
    -- query the web API roughly once per second
    if lovr.headset.getTime() - pollTime > 1 then
        pollTime = lovr.headset.getTime()
        checkForUpdates()
        pollCount = pollCount + 1
    end
        
    -- increment the spiral rotation angle
end

function lovr.draw(pass)
    _G[state](pass)
end
