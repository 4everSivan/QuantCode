import os

from typing import Dict


class Tools:

    @staticmethod
    def check_path(path: str, tp: str = 'file', not_empty: bool = True) -> Dict:
        """ Check target path is right
        :param path: target path which need to check
        :param tp: target path type
        :param not_empty: should check is dir can be empty
        :return: return check res and error msg when check failed
        """
        if not os.path.exists(path):
            err_msg = "{0} {1} does not exist".format(tp, path)
            return {'state': False, 'err_msg': err_msg}

        # read permission
        if not os.access(path, os.R_OK):
            err_msg = "{0} {1} is not readable.".format(tp, path)
            return {'state': False, 'err_msg': err_msg}

        # type
        if tp == 'file':
            if not os.path.isfile(path):
                err_msg = "{} is not a file.".format(path)
                return {'state': False, 'err_msg': err_msg}
        else:
            if not os.path.isdir(path):
                err_msg = "{} is not a directory.".format(path)
                return {'state': False, 'err_msg': err_msg}
            elif not not_empty and not os.listdir(path):
                err_msg = "directory {} is empty.".format(path)
                return {'state': False, 'err_msg': err_msg}
            else:
                if not os.access(path, os.W_OK):
                    err_msg = "{} is not writable.".format(path)
                    return {'state': False, 'err_msg': err_msg}

        return {'state': True}
