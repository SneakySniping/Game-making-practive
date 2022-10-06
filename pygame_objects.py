from colours import *
import pygame

class Button:
    def __init__(self, surface, width, height, x, y, font, font_size, text, text_colour, border_radius, bg_colour, show_bg, hover_colour, show_hover, shadow_colour, shadow_offset, show_shadow):
        pygame.init()
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, int(font_size))
        self.text = text
        self.text_colour = text_colour
        self.text_colour = list(self.text_colour)
        for i, item in enumerate(self.text_colour):
            if item < 0:
                self.bg_colour[i] = 0
        self.text_colour = tuple(self.text_colour)
        self.border_radius = border_radius
        self.bg_colour = bg_colour
        self.bg_colour = list(self.bg_colour)
        for i, item in enumerate(self.bg_colour):
            if item < 0:
                self.bg_colour[i] = 0
        self.bg_colour = tuple(self.bg_colour)
        self.show_bg = show_bg
        self.hover_colour = hover_colour
        self.hover_colour = list(self.hover_colour)
        for i, item in enumerate(self.hover_colour):
            if item < 0:
                self.hover_colour[i] = 0
        self.hover_colour = tuple(self.hover_colour)
        self.show_hover = show_hover
        self.shadow_colour = shadow_colour
        self.shadow_offset = shadow_offset
        self.show_shadow = show_shadow
        self.pressed = False

        self.rect = pygame.Rect((x, y), (width, height))
        self.rect.center = (x, y)

    def draw(self):
        self.text_surf = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        
        if self.show_shadow:
            self.shadow_rect = pygame.Rect((self.x + self.shadow_offset[0], self.y + self.shadow_offset[1]), (self.width, self.height))
            self.shadow_rect.center = (self.x + self.shadow_offset[0], self.y + self.shadow_offset[1])
            pygame.draw.rect(self.surface, self.shadow_colour, self.shadow_rect, border_radius=self.border_radius)

        if self.show_bg:
            if self.show_hover:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if self.pressed == True:
                        pygame.draw.rect(self.surface, self.hover_colour, self.shadow_rect, border_radius=self.border_radius)
                        self.text_surf = self.font.render(self.text, True, self.text_colour)
                        self.text_rect = self.text_surf.get_rect(center=self.shadow_rect.center)
                    else:
                        pygame.draw.rect(self.surface, self.hover_colour, self.rect, border_radius=self.border_radius)
                else:
                    pygame.draw.rect(self.surface, self.bg_colour, self.rect, border_radius=self.border_radius)
            else:
                pygame.draw.rect(self.surface, self.bg_colour, self.rect, border_radius=self.border_radius)
        self.surface.blit(self.text_surf, self.text_rect)
        
        

    def check_left_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True
        return False
    
    def check_right_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[3]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True
        return False
    
    def update(self, updated_text=False, updated_colour=False, updated_hover_colour=False):
        if updated_text != False:
            self.text = updated_text
        if updated_colour != False:
            self.bg_colour = updated_colour
            self.bg_colour = list(self.bg_colour)
            for i, item in enumerate(self.bg_colour):
                if item < 0:
                    self.bg_colour[i] = 0
            self.bg_colour = tuple(self.bg_colour)
        if updated_hover_colour != False:
            self.hover_colour = updated_hover_colour
            self.hover_colour = list(self.hover_colour)
            for i, item in enumerate(self.hover_colour):
                if item < 0:
                    self.hover_colour[i] = 0
            self.hover_colour = tuple(self.hover_colour)

class Label:
    def __init__(self, surface, width, height, x, y, font, font_size, initial_text, text_colour, border_radius, bg_colour, show_bg, shadow_colour, shadow_offset, show_shadow):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, font_size)
        self.text = initial_text
        self.text_colour = text_colour
        self.text_colour = list(self.text_colour)
        for i, item in enumerate(self.text_colour):
            if item < 0:
                self.text_colour[i] = 0
        self.text_colour = tuple(self.text_colour)
        self.border_radius = border_radius
        self.bg_colour = bg_colour
        self.bg_colour = list(self.bg_colour)
        for i, item in enumerate(self.bg_colour):
            if item < 0:
                self.bg_colour[i] = 0
        self.bg_colour = tuple(self.bg_colour)
        self.show_bg = show_bg
        self.shadow_colour = shadow_colour
        self.shadow_offset = shadow_offset
        self.show_shadow = show_shadow

        self.rect = pygame.Rect((x, y), (width, height))
        self.rect.center = (x, y)

        self.text_surf = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self):
        if self.show_bg:
            if self.show_shadow:
                self.shadow_rect = pygame.Rect((self.x + self.shadow_offset[0], self.y + self.shadow_offset[1]), (self.width, self.height))
                self.shadow_rect.center = (self.x + self.shadow_offset[0], self.y + self.shadow_offset[1])
                pygame.draw.rect(self.surface, self.shadow_colour, self.shadow_rect, border_radius=self.border_radius)
            pygame.draw.rect(self.surface, self.bg_colour, self.rect, border_radius=self.border_radius)
        self.surface.blit(self.text_surf, self.text_rect)
    
    def update(self, updated_text=False, updated_colour=False):
        if updated_text != False:
            self.text = updated_text
        if updated_colour != False:
            self.bg_colour = updated_colour
            self.bg_colour = list(self.bg_colour)
            for i, item in enumerate(self.bg_colour):
                if item < 0:
                    self.bg_colour[i] = 0
            self.bg_colour = tuple(self.bg_colour)

class ScrollBar:
    def __init__(self, surface, width, height, x, y, outer_border_radius, inner_border_radius, bg_colour, bar_colour, show_bg, bar_hover_colour, show_bar_hover, lines):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.outer_border_radius = outer_border_radius
        self.inner_border_radius = inner_border_radius
        self.bg_colour = bg_colour
        self.bar_colour = bar_colour
        self.show_bg = show_bg
        self.bar_hover_colour = bar_hover_colour
        self.show_bar_hover = show_bar_hover
        self.lines = lines

        self.segment_height = self.height/lines
        self.bar_width = self.width - (self.width/4)
        self.bar_height = self.segment_height
        self.top_y = self.y - self.height/2
        self.segments = []

        for i in range(self.lines):
            segment = i + 1
            self.segments.append(((self.top_y + (segment*self.segment_height) - self.segment_height), self.top_y + (segment*self.segment_height)))

        self.starting_y = self.top_y + self.bar_height/2
        self.bar_x = self.x
        self.bar_y = self.starting_y
        self.bar = ""
        self.bar = Button(self.surface, self.bar_width, self.bar_height, self.bar_x, self.bar_y, "Arial", 1, "", BLACK, self.inner_border_radius, self.bar_colour, True, self.bar_hover_colour, self.show_bar_hover, BLACK, (0, 0), False)
        self.bar_position = 0

        self.outer_rect = pygame.Rect((x, y), (width, height))
        self.outer_rect.center = (x, y)
    
    def draw(self):
        if self.show_bg:
            pygame.draw.rect(self.surface, self.bg_colour, self.outer_rect, border_radius=self.outer_border_radius)
        self.bar.draw()


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.outer_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    for i, element in enumerate(self.segments):
                        if mouse_pos[1] > element[0] and mouse_pos[1] < element[1]:
                            self.bar_position = i
                            self.bar_y = (element[0] + (element[1]-element[0])/2)
        self.bar = Button(self.surface, self.bar_width, self.bar_height, self.bar_x, self.bar_y, "Arial", 1, "", BLACK, self.inner_border_radius, self.bar_colour, True, self.bar_hover_colour, self.show_bar_hover, BLACK, (0, 0), False)

    def change_position(self, amount):
        mouse_pos = pygame.mouse.get_pos()
        if self.outer_rect.collidepoint(mouse_pos):
            if amount > 0:
                if self.bar_position != self.lines - 1:
                    self.bar_position += amount
                    self.bar_y += amount*self.segment_height
            elif amount < 0:
                if self.bar_position != 0:
                    self.bar_position += amount
                    self.bar_y += amount*self.segment_height

    def check_position(self):
        return self.bar_position + 1

class CheckBox:
    def __init__(self, surface, width, height, x, y, checked_colour, border_radius, bg_colour, show_bg):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.checked_colour = checked_colour
        self.border_radius = border_radius
        self.bg_colour = bg_colour
        self.show_bg = show_bg
        self.pressed = False
        self.checked = False
        

        self.large_rect = pygame.Rect((x, y), (width, height))
        self.large_rect.center = (x, y)

        self.small_rect = pygame.Rect((x, y), (width - width/4, height - height/4))
        self.small_rect.center = (x, y)
    
    def draw(self):
        if self.show_bg:
            pygame.draw.rect(self.surface, self.bg_colour, self.large_rect, border_radius=self.border_radius)
        
        if self.checked:
            pygame.draw.rect(self.surface, self.checked_colour, self.small_rect, border_radius=self.border_radius)
    
    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.large_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    if self.checked:
                        self.checked = False
                    else:
                        self.checked = True
        return False
    
    def get_checked(self):
        if self.checked:
            return True
        else:
            return False
