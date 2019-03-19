import os
import sublime, sublime_plugin
import datetime
_SETTING_ = sublime.load_settings("Colsavedailies.sublime-settings")
print dir(_SETTING_), type(_SETTING_)
print _SETTING_.get("daily_directory")
#print ">>>>>>>>>>>", _SETTING_.get(on_modified_field)
class Colsavedailies(sublime_plugin.WindowCommand):
    def run(self):
        print 1
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        print now
        month, day = now.split("_")
        print 111, month
        print 222, day
        root = _SETTING_.get("daily_directory")
        print "==========================", root, month, type(root), type(month)
        directory = "{0}/{1}".format(root, month)
        if not os.path.exists(directory):
            os.makedirs(directory)

        full_path = "{0}/{1}.py".format(directory, day)
        print dir(self.window.active_view())
        new_buf = self.window.active_view()
        new_buf.retarget(full_path)
        new_buf.run_command("save")
        output_view = self.window.get_output_panel("textarea")
        self.window.run_command("show_panel", {"panel": "output.textarea"})
        output_view.set_read_only(False)
        edit = output_view.begin_edit()
        if os.path.exists(full_path):
            output_view.insert(edit, output_view.size(), "saved: {}".format(full_path))
        else:
            output_view.insert(edit, output_view.size(), "save filed: {}".format(full_path))

        output_view.end_edit(edit)
        output_view.set_read_only(True)



