/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/02_with_args.yml
 *   Template: qt6/error_header.j2
 */
#pragma once
#include <QDBusError>
#include <qqmlintegration.h>

namespace gen::with_args {

/**
 * @brief Wrapper for the QDBusError class to make it accessible in QML.
 */
class DBusError : public QDBusError {
Q_GADGET

Q_ENUM(ErrorType) ///< @brief Enumeration for the error type.
Q_PROPERTY(bool isValid READ isValid CONSTANT) ///< @brief Whether this is no error.
Q_PROPERTY(QString message READ message CONSTANT) ///< @brief The error message.
Q_PROPERTY(QString name READ name CONSTANT) ///< @brief The name of the error.
Q_PROPERTY(ErrorType type READ type CONSTANT) ///< @brief The type of the error
public:
    DBusError() = default;
    DBusError(QDBusError error);
};

}