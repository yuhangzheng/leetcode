class Solution:
    def isValid(self, code: str) -> bool:
        s = code
        is_cdata = 0
        is_start_tag = 0
        is_end_tag = 0
        stack = []
        stack_of_location = []
        n = len(s)
        steps_of_jump = 0
        tag_name = ''
        have_had_a_closed_tag = 0
        for i in range(n):
            if steps_of_jump:
                steps_of_jump -= 1
                continue
            if not is_cdata:
                if is_start_tag:

                    if 'A' <= s[i] <= 'Z':
                        tag_name += s[i]
                        if 1 <= len(tag_name) <= 9:
                            continue
                        else:
                            return False
                    elif s[i] != '>':
                        return False
                    elif s[i] == '>':
                        if 1 <= len(tag_name) <= 9:
                            stack.append(tag_name)

                            is_start_tag = 0
                            tag_name = ''
                            continue
                        else:
                            return False
                elif is_end_tag:
                    if 'A' <= s[i] <= 'Z':
                        tag_name += s[i]
                        if 1 <= len(tag_name) <= 9:
                            continue
                        else:
                            return False
                    elif s[i] != '>':
                        return False
                    else:
                        if 1 <= len(tag_name) <= 9:
                            if stack and tag_name == stack.pop():
                                is_end_tag = 0
                                tag_name = ''
                                if not stack:
                                    have_had_a_closed_tag = 1
                                continue
                            else:
                                return False
                        else:
                            return False
                else:
                    if s[i] == '<':
                        if i + 1 < n and s[i + 1] == '/':
                            if not stack:
                                return False
                            is_end_tag = 1
                            steps_of_jump = 1
                            continue
                        elif i + 1 < n and s[i + 1] == '!':
                            if not stack:
                                return False
                            elif i + 8 < n and s[i:i + 9] == '<![CDATA[':
                                is_cdata = 1
                                steps_of_jump = 8
                                continue
                            else:
                                return False

                        elif i + 1 < n:
                            if have_had_a_closed_tag:
                                return False
                            is_start_tag = 1
                            continue
                        else:
                            return False
                    elif stack:
                        continue
                    else:
                        return False
            else:
                if s[i] == ']':
                    if i + 2 < n and s[i:i + 3] == ']]>':
                        steps_of_jump = 2
                        is_cdata = 0
                        continue
                    else:
                        continue
                else:
                    continue
        if is_start_tag or is_end_tag or is_cdata or stack:
            return False
        else:
            return True